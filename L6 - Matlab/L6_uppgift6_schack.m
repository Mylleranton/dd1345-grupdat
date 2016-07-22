function L6_uppgift6_schack( n )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

figure
clf
hold on
axis equal
axis([0 sqrt(n) 0 sqrt(n)]);

color = 'yellow';
for x = 1:sqrt(n)
    for y = 1:sqrt(n)
        if mod(x+y,2) == 0
            color = 'w';
        else
            color = 'k';
        end
       rectangle('Position', [x-1 y-1 1 1],'FaceColor',color); 
    end
end

end

