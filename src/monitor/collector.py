import time
from datetime import datetime
import psutil


def get_usage_info():
	now = datetime.now()
	formatted = now.strftime("%Y-%m-%d %H:%M:%S")
	return {
	"time_stamp" : formatted,
	"cpu" : psutil.cpu_percent(),
	"ram" : psutil.virtual_memory().percent
	}

	