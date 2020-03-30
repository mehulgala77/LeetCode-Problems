/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = s => {
    
    stack = [];
    
    for (let item of s) {
        if (item === "(" || item === "{" || item === "[") {
            stack.push(item);
        }
        else if (stack.length === 0) {
            return false;
        }
        else {
            poppedItem = stack.pop();
            
            if (item === ")" && poppedItem !== "(") {
                return false; 
            }
            
            if (item === "}" && poppedItem !== "{") {
                return false;
            }
            
            if (item === "]" && poppedItem !== "[") {
                return false;
            }
        }
    }
    
    return stack.length > 0 ? false : true;
};