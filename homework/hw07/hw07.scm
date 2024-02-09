(define (square n) (* n n))

(define (pow base exp) 
  (if (= exp 0)
    1
    (if (even? exp)
      (square (pow base (quotient exp 2)))
      (* base (square (pow base (quotient exp 2)))))))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
