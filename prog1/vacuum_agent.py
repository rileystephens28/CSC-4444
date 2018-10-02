from utils import *
from search import *

squares = UndirectedGraph(dict(

    state_1 =dict(right = ['state_2', 7], down =['state_4', 7], suck = ['state_10', 5]),  # square 1
    state_2 =dict(right = ['state_3', 7], left = ['state_1', 7], down =['state_5', 7], suck = ['state_19', 5]),  # square 2
    state_3 =dict (left = ['state_2', 7], down = ['state_6', 7], suck = ['state_28', 5]),  # square 3
    state_4 =dict(Up =['state_1', 7], right = ['state_5', 7], down =['state_7', 7]),  # square 4
    state_5 =dict (right = ['state_6', 7], left = ['state_4', 7], up =['state_2', 7], down =['state_8', 7]),  # square 5
    state_6 =dict (left = ['state_5', 7], up =['state_3', 7], down =['state_9', 7]),  # square 6
    state_7 =dict(right = ['state_8', 7], up =['state_4', 7]),  # square 7
    state_8 =dict (right = ['state_9', 7], up =['state_5', 7], left = ['state_7', 7]),  # square 8
    state_9 =dict (left = ['state_8', 7], up =['state_6', 7]),  # square 9

    state_10 =dict(right = ['state_11', 5], down =['state_13', 5]),  # square 1
    state_11 =dict(right = ['state_12', 5], left = ['state_10', 5], down =['state_14', 5], suck = ['state_37', 3]),  # square 2
    state_12 =dict (left = ['state_11', 5], down =['state_15', 5], suck = ['state_46', 3]),  # square 3
    state_13 =dict(Up =['state_10', 5], right = ['state_14', 5], down =['state_16', 5]),  # square 4
    state_14 =dict (right = ['state_15', 5], left = ['state_13', 5], up =['state_11', 5], down =['state_17', 5]),  # square 5
    state_15 =dict (left = ['state_14', 5], up =['state_12', 5], down =['state_18', 5]),  # square 6
    state_16 =dict(right = ['state_17', 5], up =['state_13', 5]),  # square 7
    state_17 =dict (right = ['state_18', 5], left = ['state_16', 5], up =['state_14', 5]),  # square 8
    state_18 =dict (left = ['state_17', 5], up =['state_15', 5]),  # square 9

    state_19 =dict(right = ['state_20', 5], down =['state_22', 5], suck = ['state_37', 3]),  # square 1
    state_20 =dict(right = ['state_21', 5], left = ['state_19', 5], down =['state_23', 5]),  # square 2
    state_21 =dict (left = ['state_20', 5], down =['state_24', 5], suck = ['state_55', 3]),  # square 3
    state_22 =dict(right = ['state_23', 5], up =['state_19', 5], down =['state_25', 5]),  # square 4
    state_23 =dict (right = ['state_24', 5], left = ['state_22', 5], up =['state_20', 5], down =['state_26', 5]),  # square 5
    state_24 =dict (left = ['state_23', 5], up =['state_21', 5], down =['state_27', 5]),  # square 6
    state_25 =dict(right = ['state_26', 5], up =['state_22', 5]),  # square 7
    state_26 =dict (right = ['state_27', 5], left = ['state_25', 5], up =['state_23', 5]),  # square 8
    state_27 =dict (left = ['state_26', 5], up =['state_24', 5]),  # square 9

    state_28 =dict(right = ['state_29', 5], down =['state_31', 5], suck = ['state_46', 3]),  # square 1
    state_29 =dict(right = ['state_30', 5], left = ['state_28', 5], down =['state_32', 5], suck = ['state_55', 3]),  # square 2
    state_30 =dict (left = ['state_29', 5], down =['state_33', 5]),  # square 3
    state_31 =dict(right = ['state_32', 5], up =['state_', 28], down =['state_34', 5]),  # square 4
    state_32 =dict (right = ['state_33', 5], left = ['state_31', 5], up =['state_29', 5], down =['state_35', 5]),  # square 5
    state_33 =dict (left = ['state_32', 5], up =['state_30', 5], down =['state_36', 5]),  # square 6
    state_34 =dict(right = ['state_35', 5], up =['state_31', 5]),  # square 7
    state_35 =dict (right = ['state_36', 5], left = ['state_34', 5], up =['state_32', 5]),  # square 8
    state_36 =dict (left = ['state_35', 5], up =['state_33', 5]),  # square 9

    state_37 =dict(right = ['state_38', 3], down =['state_40', 3]),  # square 1
    state_38 =dict(right = ['state_39', 3], left = ['state_37', 3], down =['state_41', 3]),  # square 2
    state_39 =dict (left = ['state_38', 3], down =['state_42', 3], suck = ['state_66', 1]),  # square 3
    state_40 =dict(right = ['state_41', 3], up =['state_37', 3], down =['state_43', 3]),  # square 4
    state_41 =dict (right = ['state_42', 3], left = ['state_40', 3], up =['state_38', 3], down =['state_44', 3]),  # square 5
    state_42 =dict (left = ['state_41', 3], up =['state_39', 3], down =['state_45', 3]),  # square 6
    state_43 =dict(right = ['state_43', 3], up =['state_40', 3]),  # square 7
    state_44 =dict (right = ['state_45', 3], left = ['state_44', 3], up =['state_41', 3]),  # square 8
    state_45 =dict (left = ['state_44', 3], up =['state_42', 3]),  # square 9

    state_46 =dict(right = ['state_47', 3], down =['state_49', 3]),  # square 1
    state_47 =dict(right = ['state_48', 3], left = ['state_46', 3], down =['state_50', 3], suck = ['state_65', 1]),  # square 2
    state_48 =dict (left = ['state_47', 3], down =['state_51', 3]),  # square 3
    state_49 =dict(right = ['state_50', 3], up =['state_46', 3], down =['state_52', 3]),  # square 4
    state_50 =dict (right = ['state_51', 3], left = ['state_49', 3], up =['state_47', 3], down =['state_53', 3]),  # square 5
    state_51 =dict (left = ['state_50', 3], up =['state_48', 3], down =['state_54', 3]),  # square 6
    state_52 =dict(right = ['state_53', 3], up =['state_49', 3]),  # square 7
    state_53 =dict (right = ['state_54', 3], left = ['state_52', 3], up =['state_50', 3]),  # square 8
    state_54 =dict (left = ['state_53', 3], up =['state_51', 3]),  # square 9

    state_55 =dict(right = ['state_56', 3], down =['state_58', 3], suck = ['state_64', 1]),  # square 1
    state_56 =dict(right = ['state_57', 3], left = ['state_55', 3], down =['state_59', 3]),  # square 2
    state_57 =dict (left = ['state_56', 3], down =['state_60', 3]),  # square 3
    state_58 =dict(right = ['state_59', 3], up =['state_55', 3], down =['state_61', 3]),  # square 4
    state_59 =dict (right = ['state_60', 3], left = ['state_58', 3], up =['state_56', 3], down =['state_62', 3]),  # square 5
    state_60 =dict (left = ['state_59', 3], up =['state_57', 3], down =['state_63', 3]),  # square 6
    state_61 =dict(right = ['state_62', 3], up =['state_58', 3]),  # square 7
    state_62 =dict (right = ['state_63', 3], left = ['state_61', 3], up =['state_59', 3]),  # square 8
    state_63 =dict (left = ['state_62', 3], up =['state_60', 3]),  # square 9

    state_64 =dict (right = ['state_65', 3]),
    state_65 =dict (right = ['state_66', 1], left =['state_64', 1]),
    state_66 =dict (left = ['state_65', 1]),
    ))

squares.percepts = dict(
    state_1=[1, 1, 1, 1], state_2 = [1, 1, 1, 2], state_3 = [1, 1, 1, 3],
    state_4=[1, 1, 1, 4], state_5 = [1, 1, 1, 5], state_6= [1, 1, 1, 6],
    state_7=[1, 1, 1, 7], state_8 = [1, 1, 1, 8], state_9 = [1, 1, 1, 9],

    state_10=[0, 1, 1, 1], state_11 = [0, 1, 1, 2], state_12= [0, 1, 1, 3],
    state_13 =[0, 0, 1, 4], state_14 = [0, 0, 1, 5], state_15 = [0, 1, 1, 6],
    state_16=[ 0, 1, 1, 7], state_17 = [ 0, 1, 1, 8], state_18= [0, 1, 1, 9],

    state_19=[1, 0, 1, 1], state_20 = [1, 0, 1, 2], state_21 = [1, 0, 1, 3],
    state_22=[1, 0, 1, 4], state_23 = [1, 0, 1, 5], state_24= [1, 0, 1, 6],
    state_25=[1, 0, 1, 7], state_26 = [1, 0, 1, 8], state_27 = [1, 0, 1, 9],

    state_28=[1, 1, 0, 1], state_29 = [1, 1, 0, 2], state_30= [1, 1, 0, 3],
    state_31=[1, 1, 0, 4], state_32 = [1, 1, 0, 5], state_33 = [1, 1, 0, 6],
    state_34=[1, 1, 0, 7], state_35 = [1, 1, 0, 8], state_36= [1, 1, 0, 9],

    state_37=[0, 0, 1, 1], state_38 = [0, 0, 1, 2], state_39 = [0, 0, 1, 3],
    state_40=[ 0, 0, 1, 4], state_41 = [0, 0, 1, 5], state_42= [0, 0, 1, 6],
    state_43 =[0, 0, 1, 7], state_44 = [0, 0, 1, 8], state_45 = [0, 0, 1, 9],

    state_46=[0, 1, 0, 1], state_47 = [0, 1, 0, 2], state_48 = [0, 1, 0, 3],
    state_49=[0, 1, 0, 4], state_50 = [0, 1, 0, 5], state_51= [0, 1, 0, 6],
    state_52 =[0, 1, 0, 7], state_53 = [0, 1, 0, 8], state_54 = [0, 1, 0, 9],

    state_55=[1, 0, 0, 1], state_56 = [1, 0, 0, 2], state_57 = [ 1, 0, 0, 3],
    state_58=[ 1, 0, 0, 4], state_59 = [ 1, 0, 0, 5], state_60= [1, 0, 0, 6],
    state_61 =[1, 0, 0, 7], state_62 = [1, 0, 0, 8], state_63 = [1, 0, 0, 9],

    state_64 = [0,0,0,0,1], state_65 = [0,0,0,0,2], state_66 = [0,0,0,0,3]
    )

def main():

    vacuum_problem = NewGraphProblem('state_5', ['state_64', 'state_65', 'state_66'], squares)
    h = memoize(vacuum_problem.h, 'h')
    [iter, node]=astar_search(vacuum_problem, lambda n:n.path_cost + h(n))
    path = node.path()
    print("State:",node.state)
    print("Action:",node.action)
    print("Path Cost =",node.path_cost)
    print("F(n) =",node.f)
    while node.parent != None:
        node = node.parent
        print("State:",node.state)
        print("Action:",node.action)
        print("Path Cost =",node.path_cost)
        print("F(n) =",node.f)

main()
