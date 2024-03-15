import { describe, test, expect } from "vitest";
import { render, screen, fireEvent } from '@testing-library/react'
import App from './App'

describe("App", () => {
  test("renders", () => {
    render(<App />);    
    expect(screen.getByText("Vite + React")).toBeDefined();
  })

  test("should increase count by 2", () => {
  
    // Act
    render(<App />);    
  
    const count = screen.getByTestId("Count");
    const button = screen.getByTestId("Increase");
  
    fireEvent.click(button);
    fireEvent.click(button);
  
    // Assert
    expect(count.textContent).toBe("2");
  });
})