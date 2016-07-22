clear all
% Definera v?r data
X = [11  12  15  28  45  52  57  75  81  88  93  97]';
Y = [1.0  1.0  1.5  6.0  9.0  10.5  11.0  16.5  9.5  8.0  12.5  12.5]';
% Definera funktionen vi ska anpassa
% har formen: y = c1*F1 + c2*F2 = c1 + x*c2
F1 = @(x) x./x;
F2 = @(x) x;

A = [F1(X) F2(X)];

% Vi f?r systemet A*c = y
c = A\Y;

% Anpassad funktion
x = linspace(min(X)-5,max(X)+5);
y = c(1) + c(2).*x;
rms = sqrt( (1./length(X)).*sum((c(1)+c(2).*X-Y).^2) );

figure
clf 
hold on
plot(X,Y,'*');
axis([min(X)-5 max(X)+5 min(Y)-5 max(Y)+5]);

plot(x,y);
text(max(X),max(Y),strcat('RMS=', num2str(rms)), 'HorizontalAlignment','right');




