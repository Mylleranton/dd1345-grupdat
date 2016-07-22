clear all
x = linspace(-5,20,1000);
y = (x.^2)/5 + 1.2.*sin(pi*x) - 3.*x.*exp(-1*x/2);

figure
clf
hold on

plot(x,y)
plot(x,0.*x)

% Avl?sning ger att funktionen har 6 nollst?llen med det minsta
% p? x = -0.23