1. Для произвольного диффура $dx = f(x,u,t)$ провести линеаризацию средствами Python/MATLAB.

Из теории:

$$
\frac{dx}{dt} = f(x, u, t) \quad - \text{наш произвольный диффур}
$$

$x_0$, $u_0$ и $t_0$ - точки

$$
f(x, u, t) \Rightarrow f_0 = f(x_0, u_0, t_0)
$$

$$
\frac{dx}{dt} \approx \frac{dx}{dt}\|\_{x=x_0} + \frac{df}{dx}\|\_{x=x_0} \cdot (x - x_0) + \frac{df}{du}\|\_{u=u_0} \cdot (u - u_0)
$$

где $\frac{df}{dx}$ и $\frac{df}{du}$ - частные производные функции $f(x, u, t)$ по $x$ и $u$ соответственно.

После уравнение будет иметь вид:

$$
\frac{dx}{dt} \approx f_0 + A \cdot (x - x_0) + B \cdot (u - u_0)
$$

где $A = \frac{\partial f}{\partial x} |\_{x=x_0}$ и $B = \frac{\partial f}{\partial u} |\_{u=u_0}$.
