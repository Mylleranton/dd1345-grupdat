clear all

% Ladda data
load('vinter.mat')
time = vinterdag(:,1) + (1/60)*vinterdag(:,2);
temp = vinterdag(:,3);


% Definera funktion
% Form: T = c1 + c2*sin(2pi*t/N) + c3*cos(2pi*t/N)
N = 24;
F1 = @(x) x./x;
F2 = @(x) sin(2*pi*x/N);
F3 = @(x) cos(2*pi*x/N);

F = [F1(time) F2(time) F3(time)];
c = F\temp;

% Anpassad kurva
x = linspace(0,24);
y = c(1) + c(2)*F2(x) + c(3)*F3(x);

figure
clf
plot(x,y);

text(max(x)-1,max(y)-1,strcat('Maxtemperatur: ', num2str(max(y))), 'HorizontalAlignment','right');

