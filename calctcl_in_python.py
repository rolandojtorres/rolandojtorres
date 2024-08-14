#con tkinter y python, creo un evaluador de codigo tcltk, que ejecuta una mini calculadora con GUI en menos de 30 lineas de codigo tcltk dentro de python
import tkinter as tk
w=tk.Tk()
code ='''
catch {destroy .c}
toplevel .c -bg #AAA
wm geometry .c "350x300+0+0"
wm withdraw .
set c 0; set col "#AAA"
place [entry .c.ev -textvar evl ] -x 50 -y 50 -width 245
foreach {t tc cmd} "0 n {0} 1 n {1} 2 n {2} 3 n {3} 4 n {4} 5 n {5} 6 n {6} 7 n {7} 8 n {8} 9 n 9 . n . pi o [expr 4*atan(1)] + o + - o - x o x / o / % o % ^ o ** C r = r {=} r {=}" {
switch $tc {
"n" {set col "#FAA"}  "o" {set col "#FFA"} "r" {set col "#AFA"}}
place [button .c.b$c -text $t -bg $col -command "append evl [set cmd]"] -x [expr 50+($c/3)*35] -y [expr (($c%3)*50)+90] -width 35
incr c
}
.c.b11 config -command {set evl [expr 4*atan(1)]}
.c.b18 config -command {set evl ""}
.c.b20 config -command {set evl [expr [string map "{M} {} {/} {*1.0/} {x} {*} {^} {**}" $evl]]}
'''
w.eval(code)
w.mainloop()
