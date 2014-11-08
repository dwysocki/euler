multOf(X, Y) :-
    Z is X mod Y,
    Z == 0.

factor(N) :- multOf(N, 3).
factor(N) :- multOf(N, 5).

%% binds S to the summation of the numbers from From to To
%% which are divisible by 3 or 5.
%%
%% ?- summation(0,10,S).
%% S = 23 .
%%
%% ?- summation(0,1000,S).
%% S = 233168 .
summation(From, To, S) :-
    From < To,
    factor(From),
    Next is From + 1,
    summation(Next, To, T),
    S is T + From.
summation(From, To, S) :-
    From < To,
    Next is From + 1,
    summation(Next, To, T),
    S is T.
summation(_, _, S) :-
    S is 0.
