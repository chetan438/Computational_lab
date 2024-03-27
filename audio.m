inputFile = '/home/master/Downloads/AUD-20240313-WA0003.mp3';
outputFile = '/home/master/Downloads/wave.wav';
[y, Fs] = audioread(inputFile);
reverse = flipud(y);
audiowrite(outputFile, reverse, Fs);
disp('Audio file reversed and saved sucessfully');
