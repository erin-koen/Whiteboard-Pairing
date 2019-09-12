// last in first out
// find max value in constant time
// assume all items are integers
// don't change push pop or peek

class MaxStack {
	constructor() {
		this.items = [];
		this.max = null;
		this.maxIndex = null;
    }
    
	getMax() {
		return this.max ? this.max : "There are no items in the stack.";
    }
    
	push(item) {
		if (this.max === null) {
			this.max = item;
			this.maxIndex = 0;
		}

		if (item > this.max) {
            this.max = item;
            // happens before push so this.items.length
			this.maxIndex = this.items.length;
		}

		this.items.push(item);
	}

	pop() {
		if (this.items.length) {
			// handle the case where there's only one item in the list
			if (this.items.length === 1) {
				this.max = null;
				this.maxIndex = null;
			}
			//if the item that's being removed is also the max, you need to assign a new max and new max index
			if (this.items.length > 1 && this.peek() === this.max) {
				let newMax = null;
				let newMaxIndex = null;
				// loop through items, find largest value and the index
				for (let i = this.items.length - 2; i >= 0; i--) {
					if (newMax == null) {
						newMax = this.items[i];
						newMaxIndex = i;
					}
					if (this.items[i] > newMax) {
						newMax = this.items[i];
						newMaxIndex = i;
					}
				}
				// adjust class values
				this.max = newMax;
				this.maxIndex = newMaxIndex;
			}
			return this.items.pop();
		}
		return null;
	}

	peek() {
		if (this.items.length) {
			return this.items[this.items.length - 1];
		}
		return null;
	}
}


const maxStack = new MaxStack();
console.log(maxStack.getMax());   // should print `null`

maxStack.push(1);
console.log(maxStack.getMax());   // should print 1

maxStack.push(100);
console.log(maxStack.getMax());   // should print 100

maxStack.pop();
console.log(maxStack.getMax());   // should print 1