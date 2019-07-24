const rotateImage = arr => {
	
    const rightColumn = arr[0].length - 1;
    const returnArr = []
    while (rightColumn >= 0){
        newArr =[]
        arr.map(i => newArr.push(i[rightColumn]))
        returnArr.push(newArr)
        rightColumn -=1
    }    

    return returnArr

};

rotateImage([
    [1, 1, 5, 9, 9],
    [2, 2, 6, 0, 0],
    [3, 3, 7, 1, 1],
    [4, 4, 8, 2, 2],
    [5, 5, 9, 3, 3]
  ]);