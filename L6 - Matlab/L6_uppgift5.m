clear all
size = 50;
particles = 5;
color = ['b', 'r', 'g', 'y', 'k', 'c', 'm', [0.5 0.5 0.5]];

figure
clf
hold on
axis([-size size -size size]);

% En partikels position defineras som en rad med x,y.
positions = zeros(particles,2);
for n = 1:250
    positions2 = positions + randn(particles,2);
    for i = 1:particles
        plot([positions(i,1) positions2(i,1)],[positions(i,2) positions2(i,2)],color(i));
    end 
    positions = positions2;
    pause(0.01)
end
hold off
