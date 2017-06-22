%%%%%%%%%%%%%%%%%%%%%% code definition %%%%%%%%%%%%%%%%%%%%%%%%%
%the code takeIs as follows it takes a 250 sample of noise (no gesture) used for calibration od system and determining noise peak and mean 
%Then it loads the train’s data and train it and gives the train model ready for prediction 
%After that it enters a while (1 ) loop where if the data get’s above the detected noise peak it begin taking a 50 samples and predict it 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
close all;
clc;
%%%%%___________ML_______________________________
trainingData = getTrainingData();
load('AllData.mat');
predictors = trainingData(:,1:end-1);
response = trainingData(:,end);

% template = templateSVM('KernelFunction', 'linear', 'PolynomialOrder', [], 'KernelScale', 'auto', 'BoxConstraint', 1, 'Standardize', 1);
% trainedClassifier = fitcecoc(predictors, response, 'Learners', template, 'Coding', 'onevsone');
trainedClassifier = fitensemble(predictors, response, 'Bag', 200, 'Tree', 'Type', 'Classification');
% Perform cross-validation
partitionedModel = crossval(trainedClassifier, 'KFold', 3);
% Compute validation accuracy
validationAccuracy = 1 - kfoldLoss(partitionedModel, 'LossFun', 'ClassifError');
validationAccuracy = validationAccuracy *100;

%%%%_______________ calibration phase __________________
a = arduino();
fprintf('Starting Calibration .... \n');
noiseData = readLearningDataGeneric(a,[0,1], 100);
maxNoisePeak1 = getNoisePeak(noiseData(1,:));
maxNoisePeak2 = getNoisePeak(noiseData(2,:));
maxNoisePeak = [maxNoisePeak1 maxNoisePeak2];
fprintf('waiting... \n');
pause(2);


while ( 1 )
    inputData1 = readVoltage(a,0); 
    inputData2 = readVoltage(a,1);
    
    if(inputData1 > maxNoisePeak(1) || inputData2 > maxNoisePeak(2))
        fprintf('Recording Geature ...');
        data50 = readLearningDataGeneric(a, [0,1], 50);
        feature50_1 = getFeature(data50(1,:), maxNoisePeak(1));
        feature50_2 = getFeature(data50(2,:), maxNoisePeak(2));
        feature50 = [feature50_1 feature50_2];
        feature50 = normalizeData(trainingSet, feature50);
        yFit = predict(trainedClassifier, feature50);
        fprintf('Your Gesture Is %d \n', yFit);
        switch(yFit)
            case 1,
                fprintf('No Gesture \n');
            case 2,
                fprintf('Like \n');
            case 3
                fprintf('I Love You \n');
            case 4
                fprintf('Yes \n');
            case 5
                fprintf('You \n');
        end
        pause();
        fprintf('Enter Your Gesure ... \n');
    end
    fprintf('Receiving Noise ... \n');
end














