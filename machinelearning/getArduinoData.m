%%%%%%%%%%%
%takes training data for each gesture and save the recorded daga in a file
%%%%%%%%%%%%
clear;
close all;
clc;
a = arduino();
dataM1NO = [];
dataM2NO = [];
for i = 1:15
    fprintf('trial no %d press enter to continue \n', i);
    pause(2);
    datatmp = readLearningDataGeneric(a, [0,1],50); 
    dataM1NO = [dataM1NO ;datatmp(1,:)];
    dataM2NO = [dataM2NO; datatmp(2,:)];
end
 save('trainingData_andrew15_NO', 'dataM1NO', 'dataM2NO');