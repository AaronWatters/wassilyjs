import { describe, it, expect } from 'vitest';
import * as main from "../lib/main.js";

describe('main module', () => {
  it('should know its name', () => {
    expect(main.name).toBe('wassilyjs');
  });
});