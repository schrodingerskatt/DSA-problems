// Problem Link : https://leetcode.com/problems/broken-calculator/


// Approach : 1. so, there are 2 options to reach target. either multiply startValue by 2 or subtract 1.
//            2. but this operation is costly.
//            3. here's why suppose, we want to convert 5 to 16. since 5 is less than 15. so our first thought will bw to increase 5.
//            4. we might end up doing something like -> 5*2 => 10*2 =>  20 - 1 => 19 - 1 => 18 - 1 => 17 - 1 => 16
//            5. total cost is => 6, it is high because everytime we multiply a number by 2 and it exceeds the target, we have 2 go alot of steps back by subtracting.
//            6. But suppose if instead of converting startValue to target, we convert our target to startValue.
//            7. then we need to divide by 2 if its even else add 1.
//            8. 16 / 2 => 8/2 => 4/2 => 2/2 => 1 + 1 => 2/2 => 1 + 1 => 2 (loop)
//            9. if you can see here we are getting stuck in  a loop and this is happening because our target is getting smaller than startValue.
//            10. if startValue becomes less than target. we have to just add (startValue - target)
//            11. 16 / 2 => 8 / 2 => 4 (stop because 4 < 5), count of steps = 2
//            12. 2 + (5 - 4) => 3 
//            13. we are adding (startValue - target)
//            14. because if value decreases than start value, we have to increase it by +1 everytime till it becomes equal to startValue.
//            15. The count of +1 here, will be same as (StartValue - target)
//            16. All we have to do now is add (StartValue - target) to count


class Solution {
public:
    int brokenCalc(int startValue, int target) {

    if(target <= startValue)
        return startValue - target;

    if(target % 2 == 0)
    return 1+ brokenCalc(startValue, target/2);
    

    return 1 + brokenCalc(startValue, target+1);


    
    }
};