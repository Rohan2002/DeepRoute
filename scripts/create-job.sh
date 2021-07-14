#!/bin/bash

srun --partition=main --mem=24000 --cpus-per-task=1 --ntasks=24 --time=4:00:00 --job-name=train-ssd-001  --pty bash
