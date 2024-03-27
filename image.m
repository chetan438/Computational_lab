inputFile = '/home/master/Pictures/Screenshot_2024-02-06_00_06_31.png';
Red = '/home/master/Pictures/r.csv';
Green = '/home/master/Pictures/g.csv';
Blue = '/home/master/Pictures/b.csv';

i = imread(inputFile);
disp(size(i));
R = i(:,:,1);
G = i(:,:,2);
B = i(:,:,3);

csvwrite(Red, R);
csvwrite(Green, G);
csvwrite(Blue, B);
disp('Image processed succesfully');
