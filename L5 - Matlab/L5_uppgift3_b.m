clear all

func = @(x) (x.^2)/5 + 1.2.*sin(pi*x) - 3.*x.*exp(-1*x/2);

fzero(func,-1)