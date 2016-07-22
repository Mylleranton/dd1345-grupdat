function fillcircle(xc,yc,r,col,n)
if nargin == 4
  n = 100;
end
fi = linspace(0,2*pi,n);
x = xc + r*cos(fi);
y = yc + r*sin(fi);
fill(x,y,col)

% G?r inte clf i funktionen, man kan vilja
% ha flera cirklar i samma bild

% nargin ger antalet anropsargument
% Om man utel?mnat sista parametern n blir nargin=4
% D? v?ljer funktionen att anv?nda n=200