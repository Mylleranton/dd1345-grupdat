function L6_uppgift4_sierpinski(x,y,n)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

if n == 0
    return
end
%pause(0.001)

M = [x(1)+(x(2)-x(1))/2 y(1)+(y(2)-y(1))/2;
     x(2)+(x(3)-x(2))/2 y(2)+(y(3)-y(2))/2;
     x(3)+(x(1)-x(3))/2 y(3)+(y(1)-y(3))/2];

x2 = M(:,1);
y2 = M(:,2);

fill(x2,y2,'white');

L6_uppgift4_sierpinski([x(1) x2(1) x2(3)], [y(1) y2(1) y2(3)],n-1);
L6_uppgift4_sierpinski([x2(1) x(2) x2(2)], [y2(1) y(2) y2(2)],n-1);
L6_uppgift4_sierpinski([x2(3) x2(2) x(3)], [y2(3) y2(2) y(3)],n-1);

end

