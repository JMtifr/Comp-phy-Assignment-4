// Assignment 4
//  Transformation method

#include <stdio.h>
#include <gsl/gsl_rng.h>
#include <math.h>
double p(double x) /* probability function */
{return 2.0*exp(-x/2.0);}
double f(double x) /* F(x) the transformation function */
{ return -2.0*log(x);}

int
main (void)
{
const gsl_rng_type * T;
gsl_rng * r;
int i, n = 10000;
double u[n],x[n];
/*---------------- generating uniform random numbers followed by transformation -----------------*/ 
gsl_rng_env_setup();
T = gsl_rng_default;
r = gsl_rng_alloc (T);
for (i = 0; i < n; i++)
{
 u[i] = gsl_rng_uniform (r);  /* random number [0,1) */
 x[i] = f(u[i]); /* random numbers distributed according to p(x) */ 
}
gsl_rng_free (r);
/*------------------------------------------------------------------------------------------------*/
/* --------------- printing random numbers in file ------------*/
FILE*fptr;
	fptr=fopen("A4_4.csv","w");
     
		for (i=0;i<n;i++)
		{
		fprintf(fptr,"%e\n",x[i]);}
		fclose(fptr);
/*---------------------------------------------------------------*/
return 0;
}
