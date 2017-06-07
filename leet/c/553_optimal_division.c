#include <stdlib.h>
#include <stdio.h>

char* optimalDivision(int* nums, int numsSize) {
	char *exp = malloc(numsSize * 10 * 2);
	int i;

	if (numsSize == 1) {
		sprintf(exp, "%d", nums[0]);
	} else if (numsSize == 2) {
		sprintf(exp, "%d/%d", nums[0], nums[1]);
	} else {
		sprintf(exp, "%d/(%d", nums[0], nums[1]);
		for (i = 2; i < numsSize; i++)
			sprintf(exp, "%s/%d", exp, nums[i]);
		sprintf(exp, "%s)", exp);
	}
	return exp;
}

int main()
{
		int nums[] = {1000, 100, 10, 2};
		printf("%s\n", optimalDivision(nums, 4));
}
