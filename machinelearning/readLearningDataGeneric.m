function [acc_data] = readLearningDataGeneric(a, pinNumber, samplesLimit )
% %%%%%%%%%%%%%%%%%%% function definition %%%%%%%%%%%%%%%%%%%%%%%%%%%
%input ; a= arduino model in matlab ;typically a=arduino
%      ;pin no. Of the analog inputs through which the circuits is connected
%      ;no_ of samples to be recorded in each trial ( aka the input window)
%out    ;matrix with 2*samplelimit (2 muscles recordings for the spiecified no. Of sample
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%-----------------------------------------

% Setup variables
acc_steps = 0 ;     % Accumulate steps (not used)
acc_data = zeros(2,samplesLimit);
step = 0.01 ;        % lowering step has a number of cycles and then acquire more data

x=0;

while ( x<samplesLimit )
    x=x+1;
    analog_val = readVoltage(a,pinNumber(1)); 
    analog_val2 = readVoltage(a,pinNumber(2));
    
    
    fprintf('anlog value 1 = %d analog value 2 =%d \n', analog_val, analog_val2);
    
    acc_data(1,x) =  analog_val  ;  
    acc_data(2,x)= analog_val2;
    plot (acc_data(1,(1:x)),'b');
    hold on;
    plot (acc_data(2,(1:x)),'r');
    
    axis([0 x 1.8 2.4]);
    acc_steps = acc_steps + step;
    drawnow;
end
close all;


end

