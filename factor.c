#include <stdio.h>

void factorize(int num) {
	printf("%d=", num);

	for (int i = 2; i <= num / 2; ++i) {
		while (num % i == 0) {
			printf("%d", i);
			num /= i;
			if (num > 1) {
				printf("*");
			}
		}
	}

	if (num > 1) {
		printf("%d", num);
	}

	printf("\n");
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <file>\n", argv[0]);
		return 1;
	}

	FILE *file = fopen(argv[1], "r");
	if (file == NULL) {
		perror("Error opening file");
		return 1;
	}

	int num;
	while (fscanf(file, "%d", &num) == 1) {
		factorize(num);
	}

	fclose(file);
	return 0;
}
