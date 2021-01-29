# frozen_string_literal: true

require "jekyll"
require "nokogiri"

module Jekyll
  class LoadingLazy
    def self.process(content)
      html = content.output
      content.output = process_tags(html) if process_tags?(html)
    end

    def self.process?(doc)
      (doc.is_a?(Jekyll::Page) || doc.write?) && doc.output_ext == ".html" ||
        doc.permalink&.end_with?("/")
    end

    def self.process_tags?(html)
      html.include?("<img")
    end

    def self.process_tags(html)
      content = Nokogiri.HTML(html)
      tags = content.css(".many-post img")
      tags.each do |tag|
        src = tag["src"]
        if src.match(/imgur/)
          tag["src"] = src.gsub(/\.jpg/, "m.jpg")
        end
      end
      content.to_html
    end

    private_class_method :process_tags
    private_class_method :process_tags?
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  Jekyll::LoadingLazy.process(doc) if Jekyll::LoadingLazy.process?(doc)
end