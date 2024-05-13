# mip-project-2024
Задание по "Моделированию информационных процессов"

1. Для произвольного диффура $dx = f(x,u,t)$ провести линеаризацию средствами python/matlab

Из теории:

$\frac{dx}{dt} = f(x, u, t)$ - наш произвольный диффур

$x_0$, $u_0$ и $t_0$ - точки
 
$f(x, u, t)$ $\Rightarrow$ $f_0 = f(x_0, u_0, t_0)$ \)


$\frac{dx}{dt} \approx \frac{dx}{dt} \bigg|_{x=x_0} + \frac{\partial f}{\partial x} \bigg|_{x=x_0} \cdot (x - x_0) + \frac{\partial f}{\partial u} \bigg|_{u=u_0} \cdot (u - u_0)$

где $\frac{\partial f}{\partial x}$ и $ \frac{\partial f}{\partial u}$ - частные производные функции $f(x, u, t)$ по $x $ и $u$ соответственно.

$\Rightarrow$ после уравнение будет иметь вид

$\frac{dx}{dt} \approx f_0 + A \cdot (x - x_0) + B \cdot (u - u_0)$

где $A = \frac{\partial f}{\partial x} \bigg|_{x=x_0}$ и $B = \frac{\partial f}{\partial u} \bigg|_{u=u_0}$