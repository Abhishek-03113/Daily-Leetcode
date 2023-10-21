function countElements(elements) {
    let counter = 0; 
    let arr = [] ;
    const cont = {} ; 

    for (let i = 0; i <= elements.length; i++)
    {   
        if (!arr.includes(elements[i]))
        {
            arr.push(elements[i]);
        }
    }

    for (let i = 0; i<elements.length;i++)
    {
        if (arr[i]== elements[i])
        {
            counter+=1;
            cont[i] = counter
        }

    }
    console.log(cont);
    
}

countElements([1,1,5,6,9,8,7,4,4,7,7])
