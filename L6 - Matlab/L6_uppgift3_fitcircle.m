function [ xc, yc, r ] = L6_uppgift3_fitcircle( X,Y )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

% Formel f?r cirkel: c1 + c2*x + c3*y = x^2 + y^2
% Fc=x2+y2=Z

X = X';
Y = Y';

F1 = @(x,y) ones(length(X),1);
F2 = @(x,y) x;
F3 = @(x,y) y;
F = [F1(X,Y) F2(X,Y) F3(X,Y)];
C = F\(X.^2 + Y.^2)

xc = C(2)./2;
yc = C(3)./2;
r = sqrt(C(1) + (C(2).^2 + C(3).^2)./4);

end

