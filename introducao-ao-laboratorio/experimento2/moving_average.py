def make_moving_average(points: list, pace: int) -> list:
    '''
    input:
        - points: list of floats representing the function points
        - pace: int used as lower and upper bound of points to calculate the average
    output:
        list of floats representing the moving average of the input points
    '''
    length = len(points)
    moving_average_points = []
    for i in range(pace, length-pace):
        sum = 0.0
        for j in range(i-pace, i+pace):
            sum+=points[j]
        average = sum/(2*pace)
        moving_average_points.append(average)
    return moving_average_points
    