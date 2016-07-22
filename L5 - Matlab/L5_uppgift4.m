clear all
alpha = 3.7415*10^(-16);
beta = 0.014388;

intensity_func = @(temp,wavelength) alpha./( wavelength.^(5).*( exp( beta./(wavelength.*temp) ) - 1 ));

lambda = 0:(0.1*10^(-6)):(10*10^(-6));
T = [600 800 1000 1100];

figure
clf
hold on
title('Intensity curves');
xlabel('Wavelength [m]');

for i = 1:length(T)
    intensity = intensity_func(T(i),lambda);
    [maxvalue, maxindex] = max(intensity);
    plot(lambda(maxindex),maxvalue,'b*')
    text(lambda(maxindex),maxvalue,strcat('T=',num2str(T(i))), 'FontSize', 12, 'VerticalAlignment', 'bottom');
    plot(lambda, intensity, 'black');
    grid on
end