clear all
X = [0 4 6.5];
Y = [1.42 6.18 4.75];

figure
clf
hold on

% Modifiera vektorerna f?r sluten figur
X = [X X(1)];
Y = [Y Y(1)];

% Sidl?ngder
s = sqrt(diff(X).^2 + diff(Y).^2);

% s1 = r1 + r2
% s2 = r2 + r3
% s3 = r3 + r1
A = [1 1 0; 0 1 1; 1 0 1];
r = A\s'
for i = 1:3
    fillcircle(X(i),Y(i),r(i),'y')
end

% Rita  triangel
fill(X,Y,'g')


