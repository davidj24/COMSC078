; David Jo. Assignment 9 "Programming in Scheme"
; Program prupose: To implement a program in scheme that is a scheme version of the summation functions we rwot ein python

(define (cube x)
    (* x x x)
)


(define (sum-integers a b)
    (if (> a b)
        0
        (+ a (sum-integers (+ a 1) b))
    )
)


(define (sum-cubes a b)
    (if (> a b)
        0
        (+ (cube a) (sum-cubes (+ a 1) b))
    )
)

(define (pi-sum n)
    (define (calculate_term k)
        (/ 8.0 (* (- (* 4 k) 3) (- (* 4 k) 1))
        )
    )

    (define (iterate k final_pi)
        (if (> k n)
            final_pi
            (iterate (+ k 1) (+ final_pi (calculate_term k)))
        )
    )

    (iterate 1 0.0)
)



; Second part where we make the single parameter functions/procedures and the higher order procedure
(define (identity x)
    x
)

(define (pi-term k)
    (/ 8.0 
        (* 
            (- 
                (* 4 k) 3
            ) 
            (- 
                (* 4 k) 1
            )
        )
    )
)



(define (generic-sum procedure lower upper)
    (if (> lower upper)
        0.0
        (+ 
            (procedure lower)
            (generic-sum 
                procedure 
                (+ lower 1) 
                upper
            )
        )
    )
)


; I'm not sure if you wanted us to reimplement the other functions int eh assignment using higher order, but it seemed implied so just in case:
(define (sum-integers-ho a b)
    (generic-sum identity a b)
)

(define (sum-cubes-ho a b)
    (generic-sum cube a b)
)

(define (pi-sum-ho n)
    (generic-sum pi-term 1 n)
)