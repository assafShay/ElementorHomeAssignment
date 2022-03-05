"""application entry point"""
import warnings
from controller import flow


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    flow.run()
