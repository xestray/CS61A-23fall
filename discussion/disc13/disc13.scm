(define (nondecreaselist s)

    (if (null? s)
        nil
        (let ((rest (nondecreaselist (cdr s)) ))
            (if (or (null? rest) (> (car s) (car (car rest))))
                (cons (list (car s)) rest)
                (cons (cons (car s) (car rest)) (cdr rest))
            )
        )
    )
)

(expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

(expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
        ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))


(define (make-long-or args)
    (cond
        ((null? args) #f)
        (else
            `(let ((value ,(car args)))
                (if value value ,(make-long-or (cdr args))))
        )
    )
)

;scm> (define or-program (make-long-or '((print 'hello) (/ 1 0) 3 #f)))
;or-program
;scm> (eval or-program)
;hello
;scm> (eval (make-long-or '((= 1 0) #f (+ 1 2) (print 'goodbye))))
;3
;scm> (eval (make-long-or '((> 3 1))))
;#t
;scm> (eval (make-long-or '()))
;#f
