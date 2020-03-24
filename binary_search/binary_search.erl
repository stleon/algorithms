-module(binary_search).
-compile([export_all]).
% -export([binary_search_start/2]).


get_middle(A, Start, End) when Start =< End ->
    Middle = (End - Start) div 2,
    {Middle, array:get(Middle, A)}.


start(Elements, X) -> 
    A = array:from_list([I || I <- lists:seq(0, Elements)], {default, 0}),
    {Start, End} = {0, array:size(A) - 1},
    {MiddleInd, MiddleVal} = get_middle(A, Start, End),
    find(A, Start, End, MiddleInd, MiddleVal, X).

find(_, Start, End, _, _, _) when Start < End -> false;
find(_, _, _, MiddleInd, MiddleVal, X) when MiddleVal == X -> MiddleInd;
find(A, Start, _, MiddleInd, MiddleVal, X) when MiddleVal > X ->
    NewEnd = MiddleInd - 1,
    {NewMiddle, NewY} = get_middle(A, Start, NewEnd),
    find(A, Start, NewEnd, NewMiddle, NewY, X);

find(A, _, End, MiddleInd, MiddleVal, X) when MiddleVal < X ->
    NewStart = MiddleInd + 1,
    {NewMiddle, NewY} = get_middle(A, NewStart, End),
    find(A, NewStart, End, NewMiddle, NewY, X).
