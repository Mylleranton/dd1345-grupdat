clear all
% Tv? matriser A, B och en vektor x
A = [2 1; 4 5];
B = [1 1; 2 3];
x = [7; 9];

% Matrisprodukterna AB och BA
C = A*B;
D = B*A;

% Elementvis multiplikation av AB, BA.
% F ?r lika med G, ty elementvis.
F = A.*B;
G = B.*A;

% Matris-vektorprodukt Ax
z = A*x;

% Multiplikation med transponat (').
p = z'*z;
E = A'*A;
q = x'*x;

% SVAR KORTFR?GOR
% a.
%   C,D,F,G,E ?r matriser
%   x,z ?r vektorer
%   p,q ?r skal?rer

% b. Skapa matris H
H = [eye(2) A; -1.*B eye(2)];

% c. Kolumn 3
H(:,3);

% d. Rad 2
H(2,:);

% e. Produkt av rad 1 och kolumn 4
H(1,:) * H(:,4);

% f. ?ndra ett element. ?ndra hel rad
H(1,1) = 1;
H(2,:) = [1 1 1 1];

% g. Inre matris (ta bort "kanterna")
J = H(2:end-1,2:end-1);

% h och i. 
K = [H ones(length(H),1)];

% j
L = [H ones(length(H),1); zeros(1,length(H)) 1];

% k
% K(:) = alla v?rden i K i f?ljd, som en kolonnvektor
% K([4 9 12]) = 4, 9 och 12e elementet fr?n K():

% l och m
p = [9 6 1 2 1 4 3 9 5 9];
p2 = p(2:end) - p(1:end-1);

% n - anv?nd .^ operatorn
% z i uppgiften bildas enligt z = x.^2 + y.^2
q = [2 2 2];
q2 = q.^2

% o 
summa = sum(K(:).^2)