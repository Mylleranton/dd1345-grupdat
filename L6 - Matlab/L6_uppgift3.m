clear all
%a
clear X Y
X = [-1 0 1];
Y = [0 1 0];
[xc, yc, r] = L6_uppgift3_fitcircle(X,Y);

figure
clf
hold on
plot(X,Y,'*')
pos = [xc-r yc-r 2*r 2*r];
rectangle('Position',pos,'Curvature',[1 1])
axis equal
title('4a');
hold off

%b
clear X Y
X = [-2 -1 2 -1 1 3];
Y = [2 5 4 0 0 1];
[xc, yc, r] = L6_uppgift3_fitcircle(X,Y);

figure
clf
hold on
plot(X,Y,'*')
pos = [xc-r yc-r 2*r 2*r];
rectangle('Position',pos,'Curvature',[1 1])
axis equal
title('4b');
hold off

%c
clear X Y
figure
clf
hold on
title('4c');
[X,Y] = ginput
[xc, yc, r] = L6_uppgift3_fitcircle(X',Y');

plot(X,Y,'*')
pos = [xc-r yc-r 2*r 2*r];
rectangle('Position',pos,'Curvature',[1 1])
axis equal

hold off
