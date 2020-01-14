#include <iostream>

#include "gtest.h"
#include "Hello.hpp"

TEST(Hello, World)
{
  Hello bob;

  bob.name = "World";

  EXPECT_EQ("Hello World", bob.getName());
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  return RUN_ALL_TESTS();
}