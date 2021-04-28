const csv = require('csv-parser');
const fs = require('fs');
const mathjs = require('mathjs');

const raw_dataset = [];
const window_size = 3;
const timeDiff = 2.78;
const window_shift = 3;

function getSlope(y,x){
    var n = y.length;
    var sum_x = 0;
    var sum_y = 0;
    var sum_xy = 0;
    var sum_xx = 0;
    var sum_yy = 0;

    for (var i = 0; i < n; i++) {

        sum_x += x[i];
        sum_y += y[i];
        sum_xy += (x[i]*y[i]);
        sum_xx += (x[i]*x[i]);
        sum_yy += (y[i]*y[i]);
    } 

    return (n * sum_xy - sum_x * sum_y) / (n*sum_xx - sum_x * sum_x);
}

function getCol(matrix, col){
    var column = [];
    for(var i=0; i<matrix.length; i++){
       column.push(matrix[i][col]);
    }
    return column;
 }

function extract_features(data){
    const feature_data = []
    const feature_labels = []
    const timeCol = getCol(data,0);
    const dataTimeDiff = timeCol[timeCol.length-1] - timeCol[0];
    let num_windows = 0;
    for(let i=0;i<=data.length-window_size;i+=window_shift){
        const feature_row = []
        const window_data = data.slice(i,i+window_size);

        const humidCol = getCol(window_data,2);
        const labelCol = getCol(window_data,3);

        //Humidity mean
        feature_row.push(mathjs.mean(humidCol));
        //Humidity slope
        feature_row.push(getSlope(humidCol, [...Array(window_size).keys()]))

        //Push features
        feature_data.push(feature_row);
        feature_labels.push(mathjs.mode(labelCol)[0])
        num_windows++;
    }
    return [feature_data, feature_labels, dataTimeDiff / 1000 / num_windows / window_size];
}

function getMaskTime(labels, mult){
    let sum = 0;
    for(const label of labels){
        if(label === 1){
            sum += 1;
        }
    }
    return sum * mult
}

function getAccuracy(predict, ground){
    let sum = 0;
    for(let i=0;i<predict.length;i++){
        if(predict[i] === ground[i]){
            sum += 1;
        }
    }
    return sum / predict.length;
}

function classifyDecisionTree(data){
    const labels = [];
    for(const entry of data){
        if(entry[0] <= 66){
            labels.push(0);
        }
        else {
            if(entry[1] <= -0.5){
                labels.push(0);
            }
            else if(entry[1] >= 0.5){
                labels.push(1);
            }
            else {
                labels.push(1);
            }
        }
    }
    return labels;
}

fs.createReadStream('data.csv')
    .pipe(csv({
        mapValues: ({ value }) => parseFloat(value)
    }))
    .on('data', (row) => {
        raw_dataset.push(Object.values(row))
    })
    .on('end', () => {
        [knn_training_data, knn_training_labels, training_diff] = extract_features(raw_dataset.slice(0,parseInt(raw_dataset.length * 0.7)));
        [knn_test_data, knn_test_labels, test_diff] = extract_features(raw_dataset.slice(parseInt(raw_dataset.length * 0.7)));
        const labels = classifyDecisionTree(knn_test_data);
        console.log('Accuracy: ' + 100 * getAccuracy(labels, knn_test_labels).toFixed(2) + '%')
        const m1 = getMaskTime(labels, test_diff)
        const m2 = getMaskTime(getCol(raw_dataset.slice(parseInt(raw_dataset.length * 0.7)),3),1);
        console.log('Mask wear time prediction: ' + m1.toFixed(2) + ' seconds');
        console.log('Mask wear time actual: ' + m2.toFixed(2) + ' seconds');
        console.log('Mask wear time percent error: '+ (100 * Math.abs(m1 - m2)/m2).toFixed(3) + '%');
    });