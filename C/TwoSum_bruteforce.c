#include <stdio.h>
#include <stdlib.h>
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
	int i, j;
	int *returnarray = malloc(sizeof(int) * 2);
	if (!returnarray)
		return NULL;
	*returnSize = 2;
	returnarray[0] = -1;
	returnarray[1] = -1;

	for (i = 0; i < numsSize; i++)
	{
		for (j = (i + 1); j < (numsSize); j++)
		{
			if (nums[i] + nums[j] == target)
			{
				returnarray[0] = i;
				returnarray[1] = j;
				return returnarray;
			}
		}
	}
	return returnarray;
}

int main()
{
	int nums[] = {2, 7, 11, 15};
	int size = 2;
	int *answer;
	answer = twoSum(nums, 4, 9, &size);
	printf("%d, %d\n", answer[0],answer[1]);
	free(answer);
	return 0;
}
