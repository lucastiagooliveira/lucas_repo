function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));
alpha = 0.01;
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%
h = X*theta;

reg = (lambda/m)*theta;

reg_1 = reg.*ones(size(reg));
reg_1(1,:) = 0;

grad = ((1/m) * X' * (h - y)) + reg_1;

%theta  = theta - alpha * grad;

reg_cost = (lambda/(2*m)) .* theta.^2;
reg_cost_1 = ones(size(reg_cost)).*reg_cost;
reg_cost_1(1) = 0;
reg_cost_1 = sum(reg_cost_1);


J = (1/(2*m))*(sum(sum((h - y).^2))) + reg_cost_1;




% =========================================================================

grad = grad(:);

end
