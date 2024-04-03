interface ExampleProps {
  exampleClass: string;
  title: string;
  children: JSX.Element;
}

function Example({exampleClass, title, children} : ExampleProps) {
  return (
    <div className="row">
        <div className={`column ${exampleClass}`}>
          <div className="flex-container">
            <div className="flex-item"></div>
            <div className="flex-item" />
            <div className="flex-item" />
          </div>
        </div>
        <div className="column">
          <h2>{title}</h2>
          {children}
        </div>
      </div>
  );
};

export default function Home() {
  return (
    <main>
      <Example exampleClass="example-1" title="Example 1">
        <p><code>flex-direction: row</code> (default)</p>
      </Example>

      <Example exampleClass="example-2" title="Example 2">
        <p><code>flex-direction: column</code></p>
      </Example>

      <Example exampleClass="example-3" title="Example 3">
        <p><code>flex-direction: row</code> and <code>justify-content: center</code></p>
      </Example>

      <Example exampleClass="example-4" title="Example 4">
        <p><code>flex-direction: row</code> and <code>justify-content: space-between</code></p>
      </Example>

      <Example exampleClass="example-5" title="Example 5">
        <p><code>flex-direction: row</code>, <code>justify-content: center</code>, and <code>flex-grow: 1</code> for second child </p>
      </Example>

      <Example exampleClass="example-6" title="Example 6">
        <p><code>flex-direction: row</code>, <code>align-items: center</code> </p>
      </Example>
      
    </main>
  );
}
