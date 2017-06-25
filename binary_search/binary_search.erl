-module(binary_search).
-compile([export_all]).
% -export([binary_search_start/2]).


get_middle(A, Start, End) when Start =< End ->
    Middle = (End - Start) div 2,
    {Middle, array:get(Middle, A)}.


start(Elements, X) -> 
    A = array:from_list([I || I <- lists:seq(0, Elements)], {default, 0}),
    Len = Elements - 1,
    Start = 0,
    End = Len,
    {Middle, Y} = get_middle(A, Start, End),
    find(A, Start, End, Middle, Y, X).


find(_, _, _, _, Y, X) when Y == X -> Y;
find(A, Start, _, Middle, Y, X) when Y > X ->
    NewEnd = Middle - 1,
    {NewMiddle, NewY} = get_middle(A, Start, NewEnd),
    find(A, Start, NewEnd, NewMiddle, NewY, X);

find(A, _, End, Middle, Y, X) when Y < X ->
    NewStart = Middle + 1,
    {NewMiddle, NewY} = get_middle(A, NewStart, End),
    find(A, NewStart, End, NewMiddle, NewY, X).
