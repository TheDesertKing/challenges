//overcomplex, nonetheless- works
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // housekeeping
    if (prices.length === 0) return 0
    let p1 = 0
    let p2 = 0
    let p3 = 1
    let len = prices.length
    let best = 0
    while (p3 < len) {
        if (prices[p3] >= prices[p2]) p2 = p3++
        if (prices[p3] < prices[p2]) {
            best+=prices[p2]-prices[p1]
            p1 = p2 = p3++
        }
    }
    best += prices[p2]-prices[p1]
    return best
};

let t1 = [1, 2, 3, 4, 5]
console.log(maxProfit(t1))
let t2 = [7,1,5,3,6,4]
console.log(maxProfit(t2))
let t3 =[7,6,4,3,1]
console.log(maxProfit(t3))