from django.shortcuts import render
from .sudoku import solve_sudoku  # Import the solve_sudoku function

def sudoku_form(request):
    grid_list = list(range(9))  # Initialize grid_list for template iteration
    if request.method == 'POST':
        # Extract the grid data from the form
        grid = []
        for i in grid_list:  # Use grid_list instead of range(9)
            row = []
            for j in grid_list:  # Use grid_list instead of range(9)
                cell_value = request.POST.get(f'cell_{i}_{j}', '0')
                row.append(int(cell_value))
            grid.append(row)
        
        # Solve the Sudoku puzzle
        if solve_sudoku(grid, 0, 0):
            return render(request, 'solver/result.html', {'grid': grid})
        else:
            error_message = "Given input is Invalid!!"
            return render(request, 'solver/sudoku_form.html', {'error_message': error_message, 'grid_list': grid_list})
    
    return render(request, 'solver/sudoku_form.html', {'grid_list': grid_list})
