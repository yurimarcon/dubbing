import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from text_utils import process_text

class TestTextUtils(unittest.TestCase):

    # Split text in minor chunks to process.
    def test_split_text (self):
        big_text = "In this class I will tell the history of Git. It all started with Kernel Linux. Kernel Linux was developed by Linus Torvald, an open source project, and he receives contributions from all over the world. Linus Torvald started developing this project at the end of the 80s, but his first version was ready in 1991. And these contributions from all over the world that the project received, they received at the time through files by email. Who knows how crazy this project is. And then unify the code for the production version. That's how it was from 1991 to 2002. When, in 2002, the project began to use a code versioner called BitKeeper. This versioner helped the Kernel Linux project a lot, especially compared to the process that was before. But even so, Linus Torvald complained a lot about various aspects, some features that he didn't have in the tool, and some gaps that could be improved. And even so, in 2005, BitKeeper started to charge a license for the use of the tool, and he did charge the license for the Kernel Linux project. But the Kernel Linux project is a project that receives contributions from several giant companies around the world. And Linus Torvald did not accept to pay for the tool, especially for the tool to have these gaps. And then he got angry when they charged him, and said, I'm going to create a tool and it's going to be better. But to develop this tool, there were some premises that needed to be met. The first was speed. The tool needed to be fast. It needed to be simple too. It also needed to have support for development in parallel with thousands of branches. We'll talk about branches throughout the course, but at this point, think that they are ramifications. So, several features working in parallel. It also needed to be completely distributed, it didn't need to depend on the project that was in a machine, specifically, and it also needed to deal well with big projects, huge projects like the Kernel Linux project, and with efficiency. So, meeting all these premises, the Git was created. And in the next class, we'll do the Git installation."
        chunks = process_text(big_text, 100)
        self.assertEqual(len(chunks), 22)

if __name__ == '__main__':
    unittest.main()