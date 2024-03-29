using DifferentialEquations
using Plots

n = 3.5
s = 11.5
fi = 3/4*pi

function f(r, p, t)
    dr = r/sqrt(n^2-1)
    return dr
end

function f2(t)
    xt = tan(fi+pi)*t
    return xt
end

r0 = s/(n+1)

theta0 = collect(LinRange(0, 2*pi, 10000))
prob = ODEProblem(f, r0, (0, 2*pi))
sol = solve(prob, saveat=theta0)

t = collect(LinRange(0.000000001, 8, 1000))
r1=[]
tetha1=[]
for i in t
    push!(r1, sqrt(i^2 + f2(i)^2))
    push!(tetha1, atan(f2(i)/i))
end

plot(sol, proj=:polar, label="катер")
plot!(tetha1, r1, proj=:polar, label="лодка")

savefig("01jl.png")

r0 = s/(n-1)

theta0 = collect(LinRange(0, 2*pi, 10000))
prob = ODEProblem(f, r0, (0, 2*pi))
sol = solve(prob, saveat=theta0)
t = collect(LinRange(0.000000001, 15, 1000))
r1=[]
tetha1=[]
for i in t
    push!(r1, sqrt(i^2 + f2(i)^2))
    push!(tetha1, atan(f2(i)/i))
end

plot(sol, proj=:polar, label="катер")
plot!(tetha1, r1, proj=:polar, label="лодка")

savefig("02jl.png")


