function [ noisePeaks ] = getNoisePeak( data )
%%%%%%%%%%%%%%%%%%%%%%%% function definition%%%%%%%%%%%%%%
%take the recoreded noise data at the begining and gives the noise peak
%%%%%%%%%%%%%%%%/%/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

noisePeaks = max(abs(data), [],2);

end

